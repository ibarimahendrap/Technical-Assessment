/**
     * Question :
     * We have a data service returning json data from another server (Server to Server), you get json-encoded as:
     * {"username":"ali","hair_color":"brown","height":1.2},{"username":"ma rc","hair_color":"blue","height":1.4},{"username":"joe","hair_color": "brown","height":1.7},{"username":"zehua","hair_color":"black","heigh t":1.8}]
      
     * In an effort to reduce transfer size, we want to transfer the data in the following json format instead:
     * {"h":["username","hair_color","height"],"d":[["ali","brown",1.2],["ma rc","blue",1.4],["joe","brown",1.7],["zehua","black",1.8]]}
     
     * Answer :
 */

const json_awal = `
    [{"username":"ali","hair_color":"brown","height":1.2},{"username":"ma rc","hair_color":"blue","height":1.4},{"username":"joe","hair_color": "brown","height":1.7},{"username":"zehua","hair_color":"black","heigh t":1.8}]
`;

function convertJson(data){
    let data_obj    = JSON.parse(data);
    let obj_key     = Object.keys(data_obj[0]);
    let json_akhir  = {h : obj_key, d : [] };

    for (const i in data_obj) {
        if (data_obj.hasOwnProperty(i)) {
            const rs        = data_obj[i];
            json_akhir.d[i] = Object.values(rs);
        }
    }

    console.log(JSON.stringify(json_akhir));
}
convertJson(json_awal);