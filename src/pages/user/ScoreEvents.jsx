import axios from "axios"
import { useState, useEffect } from "react"

const ScoreEvents = () =>{
    const [events, setEvents] = useState([])

    
    useEffect(()=>{
    

    axios.get('api/score/events',
    {
        withCredentials: true
    })
    .then(response => {
    
        const data = response['data']
        setEvents(data)
    })
    .catch(error => console.log(error))
},[])


    if (events.length>0){
    return (<div>
        {events.map((event) => {
          return <li key={event.event_id}>{event.title}</li>;
          
        })}
    </div>)
    }
    else{
        return <div>
            <p>Пока вы не принимали участие в ивентах</p>

            </div>
    }
}

export default ScoreEvents