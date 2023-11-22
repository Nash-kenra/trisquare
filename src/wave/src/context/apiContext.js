import { apiRepo } from './apiConfig';
import Localbase from 'localbase'

// Localbase framework:  https://github.com/dannyconnell/localbase 

const db = new Localbase('pangea');
db.config.debug = false; 

export const pangea = (action, process) => {
  
    const apiRepoType = apiRepo.type; 

    const basePath = apiRepo.url;

    if (apiRepoType === 'remote') {
        getRemoteData();
    }
    else {
        getEdgeData();
    }

    function getRemoteData() { 
        const referece = basePath + action;
        console.log("fetch the data from " + referece);
        fetch(referece)
            .then((response) => response.json())
            .then((data) => process(data))
            .catch((error) => console.error('Error fetching sectors:', error));
    }
    
    function getEdgeData() { 

        const data = db.collection(action).get().then(data => {
            process(data);
        });
        
    }

};
  

  