document.addEventListener('DOMContentLoaded', function() {
  const exampleModal = document.getElementById('exampleModal')
  if (exampleModal) {
    exampleModal.addEventListener('show.bs.modal', event => {
      const button = event.relatedTarget
      const id = button.getAttribute('data-bs-id')
      const info = button.getAttribute('data-bs-info')
      handledata(id, info);
    })
  }
});

async function handledata(id, info) {
  document.getElementById("plant-container").innerHTML = "";
  document.getElementById("plant-health").innerHTML = "";
  document.getElementById("ingredients").innerHTML = "";
  document.getElementById("disease-container").innerHTML = "";

  if (info === 'Plant_Information') {
    try {
      const response = await fetch(`/planta/api/plantadata/${id}/`);
      const plant = await response.json();
      const plantContainer = document.getElementById("plant-container");

      if (!plant || typeof plant !== "object") {
        console.error("Unexpected response:", plant);
        return;
      }

      const parseJsonField = (field) => {
        try {

            let fixedField = field.replace(/'\b(?!\s)/g, '"').replace(/\b(?!\s)'/g, '"');
            return JSON.parse(fixedField);
        } catch (error) {
            console.error(`Error parsing field: ${field}`, error);
            return ["Parsing error: Invalid JSON format"];
        }
    };

      const commonNames = parseJsonField(plant.plant_data_common_names);
      const edibleParts = parseJsonField(plant.plant_data_edible_parts);
      const propagationMethods = parseJsonField(plant.plant_data_propagation_methods);

      const card = document.createElement("div");

      card.innerHTML = `
      <div class="card-body">
          <h5 class="card-title">${plant.plant_data_name}</h5>
          <img src="${plant.plant_data_image}" class="img-fluid rounded-start" alt="${plant.plant_data_name}">
          <p class="text-muted">Probability: ${(plant.plant_data_probability * 100).toFixed(2)}%</p>
          <p><strong>Taxonomy:</strong> ${plant.plant_data_taxonomy}</p>
          <p><strong>GBIF ID:</strong> ${plant.plant_data_gbif_id} | <strong>iNaturalist ID:</strong> ${plant.plant_data_inaturalist_id}</p>
          <p><strong>Common Names:</strong> ${commonNames.join(", ")}</p>
          <p><strong>Edible Parts:</strong> ${edibleParts.join(", ")}</p>
          <p><strong>Propagation Methods:</strong> ${propagationMethods.join(", ")}</p>
          <p><strong>Watering:</strong> ${plant.plant_data_watering_min} - ${plant.plant_data_watering_max} (scale)</p>
          <a href="${plant.plant_data_url}" target="_blank" class="btn btn-primary btn-sm">Learn More</a>
      </div>
      `;
      plantContainer.appendChild(card);

      const response1 = await fetch(`/planta/api/plantahealth/${id}/`);
      const data1 = await response1.json();
      const percentage = data1.health_is_healthy_probability;
      const formattedPercentage = (percentage).toLocaleString(undefined, {
        style: 'percent',
        minimumFractionDigits: 2,
      });
      document.getElementById("plant-health").innerHTML = `The plant is healthy? ${data1.health_is_healthy_binary}, probability of healthy: ${formattedPercentage}`;

      const response2 = await fetch(`/planta/api/plantaingredient/${id}/`);
      const ingredients = await response2.json();
      const ingredientContainer = document.getElementById("ingredients");
      ingredients.forEach((ingredient) => {
        const possibleUnits = parseJsonField(ingredient.ingredient_possible_units);
        const card = document.createElement("div");
        card.className = ""; 

        card.innerHTML = `
            <div class="card-body">
                <hr>
                <img src="${ingredient.ingredient_img}" class="img-fluid rounded-start" alt="${ingredient.ingredient_original_name}">
                <h5 class="card-title">${ingredient.ingredient_original_name}</h5>
                <p><strong>Amount:</strong> ${ingredient.ingredient_amount} ${ingredient.ingredient_unit}</p>
                <p><strong>Possible Units:</strong> ${possibleUnits.join(", ")}</p>
                <p><strong>Consistency:</strong> ${ingredient.ingredient_consistency}</p>
                <p><strong>Estimated Cost:</strong> ${ingredient.ingredient_estimated_cost_value} ${ingredient.ingredient_estimated_cost_unit}</p>
            </div>
        `;
        ingredientContainer.appendChild(card);
      });

      if(data1.health_is_healthy_binary===false){

        const response2 = await fetch(`/planta/api/plantadesease/${id}/`);
        const diseases = await response2.json();
        const diseaseContainer = document.getElementById("disease-container");
    
        diseases.forEach(disease => {
            const diseaseCard = document.createElement("div");
            // diseaseCard.classList.add("disease-card");
            diseaseCard.innerHTML = `
                <hr>
                <h4>${disease.disease_name} (Probability: ${(disease.disease_probability * 100).toFixed(2)}%)</h4>
                <p><strong>Description:</strong> ${disease.disease_description}</p>
                <p><strong>Cause:</strong> ${disease.disease_cause || "Unknown"}</p>
                <p><strong>Common Names:</strong> ${disease.disease_common_names_disease ? disease.disease_common_names_disease.join(", ") : "N/A"}</p>
                <p><strong>Health Assessment:</strong> ${disease.disease_health_assessment}</p>
                <p><strong>Treatment (Chemical):</strong> ${disease.disease_treatment_chemical.join("<br>")}</p>
                <p><strong>Treatment (Biological):</strong> ${disease.disease_treatment_biological.join("<br>")}</p>
                <p><strong>Prevention:</strong> ${disease.disease_prevention.join("<br>")}</p>
                <a href="${disease.disease_url}" target="_blank">More Info</a>
            `;
    
            diseaseContainer.appendChild(diseaseCard);
        });


      }
      else{
        document.getElementById("modal2").style.display="none"
      }

    }
    catch (error) {
      console.error("Caught an error:", error.message);
    } finally {
        console.log("This will always execute, regardless of an error.");
    }
  }

}

