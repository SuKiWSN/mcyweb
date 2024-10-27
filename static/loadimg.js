function decodeImage(videoUrl, data, title, price, type2, imgUrl){
    const Ee = Rr("2020-zq3-888");
    var Ar = 100;
    var reader = new FileReader();
    reader.readAsArrayBuffer(data);
    reader.onload = function(){
        var content = this.result;
        var u = new Uint8Array(content);
        for(var i=0;i<Ar;i++){
            u[i] ^= Ee[i%Ee.length];
        }
        const a = jr(u);
        var e =  `data:image/png;base64,${a}`;
        createLink(videoUrl, e, title, price, type2, imgUrl);
    }
}
function Rr(r) {
    const e = [], t = r.length;
    for (let s = 0; s < t; s++) {
        const n = r.charCodeAt(s);
        n >= 65536 && n <= 1114111 ? (e.push(n >> 18 & 7 | 240), e.push(n >> 12 & 63 | 128), e.push(n >> 6 & 63 | 128), e.push(n & 63 | 128)) : n >= 2048 && n <= 65535 ? (e.push(n >> 12 & 15 | 224), e.push(n >> 6 & 63 | 128), e.push(n & 63 | 128)) : n >= 128 && n <= 2047 ? (e.push(n >> 6 & 31 | 192), e.push(n & 63 | 128)) : e.push(n & 255)
    }
    return e
}
function jr(r) {
    let e = "";
    for (let t = r.byteLength, s = 0; s < t; s++)
        e += String.fromCharCode(r[s]);
    return self.btoa(e)
}
//<div style="float: left"><a href="http://www.baidu.com"><img src="{% static 'aaa.jpg' %}"></a></div>
function createLink(videoUrl, imgUrl, title, price, type2, imgurl){
    let favorite = document.createElement('button');
    favorite.setAttribute('style', 'width: 70px; height: 70px; position: absolute; font-size: 50px; border: none; margin: auto;')
    favorite.setAttribute('id', imgurl);
    favorite.setAttribute('onclick', `submitlike(${videoUrl}, "${imgurl}", "${title}", ${price})`);
    favorite.textContent = '❤️';
    let div = document.createElement("div");
    div.appendChild(favorite);
    let a = document.createElement("a")
    a.href = "javascript:void(0)";
    a.setAttribute("onclick", `getvideo(${videoUrl})`);
    let img = document.createElement("img");
    img.src = imgUrl;
    a.appendChild(img)
    let titlediv = document.createElement("div");
    titlediv.textContent = title;
    div.appendChild(a)
    let pricediv = document.createElement("div");
    pricediv.textContent = price;
    pricediv.setAttribute("style", "color: red;")
    div.appendChild(pricediv);
    div.appendChild(titlediv);
    parentdiv = document.getElementsByClassName(`container${type2}`)[0];
    parentdiv.appendChild(div)
}
function getpic(videoUrl, imgUrl, title, price, type2){
    let xhr = new XMLHttpRequest();
    xhr.open('get', imgUrl, true);
    xhr.responseType = 'blob';
    xhr.onload = function(){
        decodeImage(videoUrl, xhr.response, title, price, type2, imgUrl);
    }
    xhr.send();
}
function getvideo(videoUrl) {
    $.ajax(
        {
            url: '/getvideo/',
            type: "POST",
            dataType: 'json',
            data: {"videoId": videoUrl},
            success: function(data){
                data = data.data
                videoUrl = "https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?" + data;
                window.open(videoUrl, "_self");
            }
        }
    )
}
function changetype(type){
    type2 = type;
    for(var i = 0; i < count.length; i++) {
        if(i != type && count[i] != 0){
            document.getElementsByClassName(`container${i}`)[0].style.display = "none";
        }
        document.getElementsByClassName(`container${type}`)[0].style.display = "block";
    }
    if(!count[type]) add_list();
}
function submitlike(videoUrl, imgurl, title, price){
    $.ajax({
        url: '/submitlike/',
        type: 'POST',
        dataType: 'json',
        data: {"videoUrl": videoUrl, "imgurl": imgurl, "title": title, "price": price},
        success: function(data){
            console.log(data);
        }
    })
}