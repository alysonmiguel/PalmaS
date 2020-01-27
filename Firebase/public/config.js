const firebaseConfig = {
    apiKey: "AIzaSyA45MQf2Ig_xx0Er8eynM3r2KL6CeQlw2U",
    authDomain: "teste-ab9eb.firebaseapp.com",
    databaseURL: "https://teste-ab9eb.firebaseio.com",
    projectId: "teste-ab9eb",
    storageBucket: "teste-ab9eb.appspot.com",
    messagingSenderId: "862533329365",
    appId: "1:862533329365:web:b58f5c957fe12c4d8edd5c",
    measurementId: "G-STFVMB377Q"
  };
 
var fire = firebase.initializeApp(firebaseConfig);

var storage = fire.storage()
var storageRef = storage.ref();

$('#List').find('tbody').html('');

var i = 0;

storageRef.child('/imagens').listAll().then(function(result){
  result.items.forEach(function(imageRef){

   // console.log("Referencia da imagem"+ imageRef.toString());
  i++;
  displayImage(i,imageRef);
  
  });
});

function displayImage(row, images){
  images.getDownloadURL().then(function(url){
    console.log(url);

    let new_html = '';
    new_html += '<tr>';
    new_html += '<td>';
    new_html += row;
    new_html += '</td>';
    new_html += '<td>';
    new_html += '<img src="'+url+'" width="100px" style="float:right">';
    new_html += '</td>';
    new_html += '</tr>';
    $('#List').find('tbody').append(new_html);


  

  });
}
