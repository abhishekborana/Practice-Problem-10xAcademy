var data=["5","1","2","2","3","3","3"]

var res= [];
if(data.length===0 || data.length===1){
	console.log(-1);
} else {
var con=2;
var con2=1;
for(let i=2;i<data.length;i++){
	if(parseInt(data[i])===parseInt(data[i-1])){
		con2+=1;
	} 
	else{ 
		if(con2>=con){
			if(con2==con){
				res.push(parseInt(data[i-1]));
			} else{
			con=con2;
			res.push(parseInt(data[i-1]));
			}
		}
		con2=1;
	}
}
if(con2>con){
	console.log(parseInt(data[data.length-1]));
}else if(con2==con){
	res.push(parseInt(data[data.length-1]));
	for(let i=0;i<res.length;i++){
	console.log(res[i]);}
} 
else {
if(res.length===0){
	for(let i=1;i<data.length;i++){
		console.log(parseInt(data[i]));
	}
}
else{
for(let i=0;i<res.length;i++){
	console.log(res[i]);
}
}
}
}