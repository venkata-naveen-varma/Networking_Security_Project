var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Cookie", "csrftoken=AvD0utOSknFCtXKGmuzVVRkOCQ21y8SdDPRidiS8GQnJrUTxxPyLvFC55gR1Bv8V");

var raw = JSON.stringify({
  "humidity": "98f634695766c1f9403a16a5f6e0439e",
  "temperature": "a0dcb30d1d5d77353405ec4d1ce4c30b",
  "sent_by": "dbf1990f5e4a9ed301ec0f9cbf925fa544f3b823ebf3469d2785d83a3e1b48c4",
  "timestamp": "fffeb4cfd6b329366fc0ee9fb786f9d75caf5bfffc1a8144283cabb56f04a74082ce182f166a237d"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://localhost:5000/process_data", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));