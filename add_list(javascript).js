let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var res=[];
for(var i=1;i<data.length;i=i+2){
	var carry=0;
	var n1 = data[i].split(" ");
	var n2 = data[i+1].split(" ");
	var num1 = n1.join("");
	var num2 = n2.join("");
	if(num2.length>num1.length){
		var temp = num1;
		num1=num2;
		num2=temp;
	}
	var n="";
	let j;
	for(j=0;j<num2.length;j++){
		var m = parseInt(num2[j])+parseInt(num1[j])+carry;
		if(m>9){
			var t =(m%10).toString();
			n+=t;
			carry= parseInt(m/10);
		} else {
			var t=m.toString();
			carry=0;
			n+=t;
		}
	}	
	for(var k=j;k<num1.length;k++){
		var m = parseInt(num1[k])+carry;
		if(m>9){
			var t =(m%10).toString();
			n+=t;
			carry= parseInt(m/10);
		} else {
			var t=m.toString();
			carry=0
			n+=t;
		}	
	}
	if(carry>0){
		n+=(carry).toString();
	}
	//console.log(n);
	res.push(n);
}
for(let i=0;i<res.length;i++){
	console.log(res[i]);
}