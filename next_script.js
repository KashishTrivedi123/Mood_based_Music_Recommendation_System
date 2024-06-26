$(document).ready(function() {
    $('#moodButton').on('click', function() {
        window.open('http://localhost:8504/mood'); // Replace with the URL of your Streamlit app for mood selection
    }).css({
        'background-color': 'purple', // Change to your desired background color
        'color': '#FFFFFF', // Change to your desired text color
        'font-size': '24px', // Change to your desired font size
        'width': '200px', // Change to your desired width
        'height': '60px' // Change to your desired height
      
    }).addClass('custom-button');
    
    $('#faceButton').on('click', function() {
        window.open('http://localhost:8502/face'); // Replace with the URL of your Streamlit app for face selection
    }).css({
        'background-color': 'purple', // Change to your desired background color
        'color': 'white', // Change to your desired text color
        'font-size': '24px', // Change to your desired font size
        'width': '200px', // Change to your desired width
        'height': '60px' // Change to your desired height
        
    }).addClass('custom-button');
    
    $('#locationButton').on('click', function() {
        window.open('http://localhost:8503/location'); // Replace with the URL of your Streamlit app for location selection
    }).css({
        'background-color': 'purple', // Change to your desired background color
        'color': '#FFFFFF', // Change to your desired text color
        'font-size': '24px', // Change to your desired font size
        'width': '200px', // Change to your desired width
        'height': '60px' // Change to your desired height
        
    }).addClass('custom-button');

    $('.custom-button').css({
       
        'border-radius': '10px', // Change to your desired border radius (for button shape)
        'margin': '10px 0' // Change to your desired vertical and horizontal spacing between buttons
        
    });
});
