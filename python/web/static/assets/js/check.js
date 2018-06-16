jQuery(function(){
    if (typeof web3 === 'undefined') {
        alert("Включите Metamask")
    }
    else {
        var checkchainContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_hash","type":"string"},{"name":"_firstName","type":"string"},{"name":"_lastName","type":"string"}],"name":"addCert","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_hash","type":"string"}],"name":"checkCert","outputs":[{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"x","type":"bytes32"}],"name":"bytes32ToString","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"source","type":"string"}],"name":"stringToBytes32","outputs":[{"name":"result","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]).at("0xa9ab1fc68dc9ec26d8c2a2c01f780a71919a111b");	
    checkchainContract.checkCert.call("12t3",(e,r)=>{console.log(r)})

    }

}
)