var address = require("address");


ip_address = address.ip()
ipv6_address = address.ipv6()
mac_address = null;


address.mac(function (err, addr) {
    mac_address = addr // '78:ca:39:b0:e6:7d'
  });


add = {"ip_address":ip_address, "ipv6_address":ipv6_address, "mac_address":mac_address};

const fs = require("fs");

const savedata = (add)=>{
  const finished = (error) =>{
    if(error){
      console.error(error)
      return;
    }
  }
  const add_json = JSON.stringify(add)
  fs.appendFileSync("network.json",add_json)
}

savedata(add)

