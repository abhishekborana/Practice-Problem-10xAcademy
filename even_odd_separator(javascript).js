data =["2 5 4 10 1 3 7 8 11 13 6"];
var odd=[];
var even=[];
var main = data[0].split(" ");
for(let i=0;i<main.length;i++){
	let j = parseInt(main[i]);
	if(j%2===0){
		even.push(j);
	} else {
		odd.push(j);
	}
}
var list = odd.concat(even);
//console.log(...list);