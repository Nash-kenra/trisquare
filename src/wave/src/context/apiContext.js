import { apiRepo } from './apiConfig.js';

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
        
        fetch(referece)
            .then((response) => response.json())
            .then((data) => process(data))
            .catch((error) => console.error('Error fetching sectors:', error));
    }
    
    function getEdgeData() { 
        return "";
    }

};
  

  