<template>
	<div>
    <h1>PMROA</h1>
		<h3>Predict Movie Revenue of Actors</h3>
    <div v-for="actor in actors" :key="actor.id" :actor="actor"
    >
		<span @click="pickActor">{{ actor }}</span>
		</div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PredictMovieView',
  data() {
    return {
      pick_actor: null,
      pick_actors:[]
    }
  },
  methods: {
    pickActor() {
      const pick_actors = this.pick_actors
      const pick_actor = this.pick_actor
      if (pick_actors.len >= 4){
        alert('4명까지만 선택해주세요')
      }
      if(pick_actor in pick_actors){
        alert('이미 선택된 배우입니다')
        this.pick_actor = null
      }else{
        pick_actors.push(pick_actor)
      }
    },
  
    movieRevenue(){
      const pick_actors = this.pick_actors

      

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/predicts/`,
        data: {
          pick_actors
        }
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })

    }
  }
}
</script>
