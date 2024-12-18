document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll(".card__btn");
  buttons.forEach((button) => {
    button.addEventListener("click", handledata);
  });
});

function handledata(event) {

  const button = event.target;
  const buttonId = button.dataset.id; 
  const info = button.dataset.info;  
  console.log("id....  " + buttonId);
  console.log("info....  " + info);
  const plantImageElement = document.getElementById('image');   
  const name = document.getElementById('name');  
  const name1 = document.getElementById('name1');  
  const text = document.getElementById('text');
  const text1 = document.getElementById('text1');
  const wiki = document.getElementById('wiki');
  const title_ingredient = document.getElementById('title_ingredient');
  const disease_list = document.getElementById('disease-list');
  plantImageElement.scr = '';
  name.innerHTML = '';
  name1.innerHTML = '';
  text.innerHTML = '';
  text1.innerHTML = '';
  wiki.innerHTML = '';
  title_ingredient.innerHTML = '';
  disease_list.innerHTML = '';

  if(info=== 'more-data') {

    fetch(`/planta/api/plantadata/${buttonId}/`)
    .then(response => response.json())
    .then(data => {
    name.textContent = `Name: ${data.plant_data_name}`;
    text.textContent = `Probability is plant: ${data.plant_data_probability}, Propagation ${data.plant_data_propagation_methods}`;
    wiki.innerHTML = 'wiki link';
    wiki.href = data.plant_data_url;
    plantImageElement.src = data.plant_data_image;
    })

    .catch(error => {
      console.log('Error:', error);
    });

    fetch(`/planta/api/plantahealth/${buttonId}/`)
    .then(response => response.json())
    .then(data => { 
    const name = document.getElementById('name');
    const percentage = data.health_is_healthy_probability;
    const formattedPercentage = (percentage).toLocaleString(undefined, {
      style: 'percent',
      minimumFractionDigits: 2,
    });
    plantImageElement.innerHTML = '';
    name1.textContent = `The plant is healthy? ${data.health_is_healthy_binary}.`;  
    text1.textContent = `probability of healthy: ${formattedPercentage}`;  
      if(data.health_is_healthy_binary===false){
        const moreInfoButton = document.createElement('button');
        moreInfoButton.textContent = 'Diseases';
        moreInfoButton.className = 'card__btn'; 
        moreInfoButton.dataset.bsToggle = 'modal'; 
        moreInfoButton.dataset.bsTarget = '#staticBackdrop'; 
        text1.appendChild(moreInfoButton); 

        const modal1 = new bootstrap.Modal(document.getElementById('staticBackdrop'));
          fetch(`/planta/api/plantadesease/${buttonId}/`)
          .then(response => response.json())
          .then(data => { 
          data.forEach(disease => {
            const listItem = document.createElement('li');
            listItem.textContent = `Name: ${disease.disease_name} Description: ${disease.disease_description}.`;
            disease_list.appendChild(listItem);
          });
          })
        .catch(error => {
          console.log('Error:', error);
      });    

        moreInfoButton.addEventListener('click', () => {
          modal1.show(); 
        });
          
    }
      })    

  }   

  if(info=== 'more_data2') {
    title_ingredient.textContent = `More info on : `+ buttonId ;
}

  if(info=== 'close') {
      setTimeout(function() {
        window.location.reload();
      }, 3000)
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
   
};


