
$.ajax(
  { url: 'https://s3.amazonaws.com/BUCKET_SITE/data.json',
   dataType: 'json',
   crossDomain: true,
   success: function (data) {
      console.log(data);
      createTable(data);
      }
  })

  function createTable(data) {
    photoanalysed = document.createElement("img");
    photoanalysed.height = 100;
    photoanalysed.width = 68;
    photoanalysed.src = 'https://s3.amazonaws.com/BUCKET_IMAGE/' + '_analyse1' + '.jpg';

    for (var data of data) {
      var trTabela = document.createElement("tr");
      var tdInfoFoto = document.createElement("td");
      var tdInfoNome = document.createElement("td");
      var tdInfoFaceMatch = document.createElement("td");
      tdInfoNome.textContent = data.nome;
      tdInfoFaceMatch.textContent = data.faceMatches;
      tdInfoFoto = document.createElement("img");
      tdInfoFoto.height = 100;
      tdInfoFoto.width = 68;
      tdInfoFoto.src = 'https://s3.amazonaws.com/BUCKET_IMAGE/' + data.nome + '.jpg';
      trTabela.appendChild(tdInfoFoto);
      trTabela.appendChild(tdInfoNome);
      trTabela.appendChild(tdInfoFaceMatch);
      var tabela = document.querySelector("#table-s3");
      tabela.appendChild(trTabela);
    }
    var photo = document.querySelector("#photo");
    photo.appendChild(photoanalysed)

  }
