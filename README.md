README


Existem três programas utilizados para gerar o modelo de testes. Get_training_images.ipynb, train_model.ipynb e test_model.ipynb. O programa que faz a classificação é o ‘test_model.ipynb’. Mas vou explicar como funcionam os três programas e os métodos que utilizei para chegar no resultado.


O primeiro programa get_training_images faz a captura de imagens pela webcam. Ele funciona da seguinte maneira:
Em 
  



Deve-se escolher quantas imagens quer registrar para o treinamento e em image_label deve-se escrever qual a categoria das imagens. ‘Down’ para sinalização negativa e ‘up’ para sinalização positiva.


Uma janela irá abrir com o vídeo da webcam. Para começar a salvar as fotos é necessário apertar a tecla ‘s’. Se desejar sair do programa aperte ‘q’.


Quando quiser trocar a classe basta mudar ‘image_label’ no programa e rodar novamente.


Abaixo está um printscreen da janela de captura de imagens.
  



O segundo programa ‘train_model.ipynb’ é o de treinamento. Nele foi utilizado tensorflow com o algorítmo de classificação SqueezeNet. SqueezeNet é um modelo pré treinado para a classificação de imagens. Foi usada a biblioteca Keras para fazer o treino das imagens.


Os principais parâmetros usados no treino foram: ‘Sequential’ foi usado um modelo sequencial, onde as camadas estão ordenadas em sequência; ‘Adam’ foi usado como optimizer; ‘number of epochs’ foi igual a 15; ‘ReLU’ foi usado como função de ativação.


Depois de treinado o modelo de treino é salvo com o nome de ‘treinamento_gestos.h5’. Ele será chamado no programa de testes. 


  



O programa de teste é o ‘test_model.ipynb’. Ele é o responsável pela classificação das imagens. Inicialmente é importado o modelo de treino ‘‘treinamento_gestos.h5’.


Para o teste foi usado o mesmo programa que capturou as imagens do treino para capturar as imagens do teste, mudando apenas o diretório onde as imagens foram salvas. Foi criado um vetor ‘answer’ contendo as respostas das imagens a serem testadas para futura avaliação do método.


O programa carrega as imagens salvas na pasta ‘test_images’ que estão em formato ‘.jpg’ e garante que elas estão no mesmo tamanho que as imagens que foram treinadas. Então, o modelo faz a predição das imagens e salva elas em um vetor ‘predict’. O vetor ‘predict’ é então comparado com o vetor ‘answer’ e são feitos o Classification Report e a Matriz Confusão, como mostra a imagem abaixo.