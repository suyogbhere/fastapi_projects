import { useEffect, useState } from "react";
import React  from "react";
import axios from 'axios';



const ResumeList= () =>{
    const [resumes, setResumes] = useState([]);
    useEffect{() => {
        const fetchResumes = async () => {
        try{
            const res = await axios.get('http://localhost:8000/resumes');
            setResumes(res.data);
            } catch(error){
                console.error('Error fetching resumes:', error);
                }
            };
            fetchResumes();
        }

    }
    return(
        <div>ResumeList</div>
    )
}


export default ResumeList


