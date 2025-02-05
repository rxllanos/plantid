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
  if (info === 'Plant_Information') {
    try {
      const response = await fetch(`/planta/api/plantadata/${id}/`);
      const plant = await response.json();
      const plantContainer = document.getElementById("plant-container");

      if (!plant || typeof plant !== "object") {
        console.error("Unexpected response:", plant);
        return;
      }

      // Function to safely parse JSON fields
      const parseJsonField = (field) => {
          try {
              return JSON.parse(field.replace(/'/g, '"'));
          } catch (error) {
              console.error(`Error parsing field: ${field}`, error);
              return [];
          }
      };

      const commonNames = parseJsonField(plant.plant_data_common_names);
      const edibleParts = parseJsonField(plant.plant_data_edible_parts);
      const propagationMethods = parseJsonField(plant.plant_data_propagation_methods);

      const card = document.createElement("div");
      card.className = "card mb-4 shadow-sm full-width-card";

      card.innerHTML = `
          <div class="row g-0">
              <div class="col-md-4">
                  <img src="${plant.plant_data_image}" class="img-fluid rounded-start" alt="${plant.plant_data_name}">
              </div>
              <div class="col-md-8">
                  <div class="card-body">
                      <h5 class="card-title">${plant.plant_data_name}</h5>
                      <p class="text-muted">Probability: ${(plant.plant_data_probability * 100).toFixed(2)}%</p>
                      <p><strong>Taxonomy:</strong> ${plant.plant_data_taxonomy}</p>
                      <p><strong>GBIF ID:</strong> ${plant.plant_data_gbif_id} | <strong>iNaturalist ID:</strong> ${plant.plant_data_inaturalist_id}</p>
                      <p><strong>Common Names:</strong> ${commonNames.join(", ")}</p>
                      <p><strong>Edible Parts:</strong> ${edibleParts.join(", ")}</p>
                      <p><strong>Propagation Methods:</strong> ${propagationMethods.join(", ")}</p>
                      <p><strong>Watering:</strong> ${plant.plant_data_watering_min} - ${plant.plant_data_watering_max} (scale)</p>
                      <a href="${plant.plant_data_url}" target="_blank" class="btn btn-primary btn-sm">Learn More</a>
                  </div>
              </div>
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


      if(data1.health_is_healthy_binary===false){
        const response2 = await fetch(`/planta/api/plantadesease/${id}/`);
        const diseases = await response2.json();

        const diseaseContainer = document.getElementById("disease-container");
        
        diseases.forEach(disease => {
          const card = document.createElement("div");
          card.className = "card mb-4 shadow-sm full-width-card";

          const parseJsonField = (field) => {
            try {
                return JSON.parse(field.replace(/'/g, '"'));
            } catch (error) {
                console.error(`Error parsing field: ${field}`, error);
                return [];
            }
        };

          const chemicalTreatment = parseJsonField(disease.disease_treatment_chemical).join(" ");
          const biologicalTreatment = parseJsonField(disease.disease_treatment_biological).join(" ");
          const preventionList = parseJsonField(disease.disease_prevention);

          card.innerHTML = `
              <div class="card-body">
                  <h5 class="card-title">${disease.disease_name}</h5>
                  <p class="text-muted">Probability: ${(disease.disease_probability * 100).toFixed(2)}%</p>
                  <p class="card-text">${disease.disease_description}</p>
                  <a href="${disease.disease_url}" target="_blank" class="btn btn-primary btn-sm">Learn More</a>
                  <hr>
                  <h6 class="text-success">Treatment</h6>
                  <p><strong>Chemical:</strong> ${chemicalTreatment}</p>
                  <p><strong>Biological:</strong> ${biologicalTreatment}</p>
                  <h6 class="text-info">Prevention</h6>
                  <ul>
                      ${preventionList.map(item => `<li>${item}</li>`).join("")}
                  </ul>
              </div>
          `;
          diseaseContainer.appendChild(card);

      });
      }

    }
    catch (error) {
      console.error("Caught an error:", error.message);
    } finally {
        console.log("This will always execute, regardless of an error.");
    }
  }


  if(info=== 'Delete') {
    const shouldDelete = confirm('Are you sure you want to delete this plant?');
    if (shouldDelete) {
      try {
          const response = fetch(`/planta/api/planta/${buttonId}/`, {
              method: 'DELETE',
          });

          if (response.ok) {
              console.log('Plant deleted successfully!');
          } else {
              console.error('Error deleting plant:', response.statusText);
          }
      } 
      catch (error) {
          console.error('An error occurred while deleting the plant:', error);
      }
    } else {
      console.log('Deletion canceled.');  
  }
      setTimeout(function() {
        window.location.reload();
      }, 100)
  }   

}

