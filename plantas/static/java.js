document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#plant-data').style.display = 'none';
  document.querySelector('#carouselExampleCaptions').style.display = 'none';
  const buttons = document.querySelectorAll(".btn");
  buttons.forEach((button) => {
    button.addEventListener("click", handledata);
  });

  $(document).ready(function(){
      $('#carouselExampleCaptions').carousel({
          interval: 2000,  // Adjust the interval (in milliseconds) to control the slide duration
          pause: 'hover'   // Pauses the carousel on mouse hover
      });
  });  
});

function handledata(event) {
  document.querySelector('#plant-data').style.display = 'none';
  document.querySelector('#carouselExampleCaptions').style.display = 'none';
  const button = event.target;
  const buttonId = button.dataset.id; 
  const info = button.dataset.info;  
  console.log("id:" + buttonId);
  console.log("info" + info);
  const plantImageElement = document.getElementById('image');   
  const name = document.getElementById('name');  
  const text = document.getElementById('text');
  const wiki = document.getElementById('wiki');
  const disease_list = document.getElementById('disease-list');
  plantImageElement.scr = '';
  name.innerHTML = '';
  text.innerHTML = '';
  wiki.innerHTML = '';
  disease_list.innerHTML = '';

  if(info=== 'more-data') {
    document.querySelector('#plant-data').style.display = 'block';
    fetch(`/planta/api/plantadata/${buttonId}/`)
    .then(response => response.json())
    .then(data => {
    name.textContent = `Name: ${data.plant_data_name}`;
    text.textContent = `Probability: ${data.plant_data_probability}, Common Names: ${data.plant_data_common_names}, Propagation ${data.plant_data_propagation_methods}`;
    wiki.innerHTML = 'wiki link';
    wiki.href = data.plant_data_url;
    plantImageElement.src = data.plant_data_image;
    })
    .catch(error => {
      console.log('Error:', error);
  });
  }   

  if(info=== 'Recepy') {
    document.querySelector('#carouselExampleCaptions').style.display = 'block';

  }   


  if(info=== 'Health') {
    document.querySelector('#plant-data').style.display = 'block';
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
    name.textContent = `The plant is healthy? ${data.health_is_healthy_binary}.`;  
    text.textContent = `probability of healthy: ${formattedPercentage}`;  
    if(data.health_is_healthy_binary===false){
      const moreInfoButton = document.createElement('button');
      moreInfoButton.textContent = 'Click for Disease data';
      moreInfoButton.className = 'btn-primary'; 
      moreInfoButton.dataset.bsToggle = 'modal'; 
      moreInfoButton.dataset.bsTarget = '#staticBackdrop'; 
      text.appendChild(moreInfoButton); 

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
    .catch(error => {
      console.log('Error:', error);
    });

  }   

  if(info=== 'close') {

    setTimeout(function() {
      window.location.reload();
    }, 200)


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
      }, 3000)
} 
   
};


