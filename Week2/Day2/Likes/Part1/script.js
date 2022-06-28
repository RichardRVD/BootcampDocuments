function addLike(){
    var like = document.getElementById('likes').innerText
    like++;
    document.getElementById('likes').innerText = like;
}