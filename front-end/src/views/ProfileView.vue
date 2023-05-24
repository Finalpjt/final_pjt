<template>
  <div>
    <h1>Profile</h1>
    사용자명 : {{ username }}
    <br>
    사용자 이메일 : {{ email }}
    <br>
    <!-- 사용자 닉네임 : {{ nickname }} -->
    <router-link to="/PasswordChangeView">changepassword</router-link>
    <div class="row row-cols-1 row-cols-md-5 g-4">
    <div
    v-for="like_movie in like_movies" :key="like_movie.id" :movie="movie"
    >
    <div class="card" @click="reload()">
      
        <router-link :to="{
          name: 'DetailView',
          params: {id: like_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${like_movie.poster_path}`" alt="" srcset="">
          
          </div>
        </router-link>
    
    </div>
    
    </div>
    </div>
    <MovieRecommendProfile v-bind:like_movies="like_movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommendProfile from '@/components/MovieRecommendProfile.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',

  components: {
    MovieRecommendProfile
  },

  data() {
    return {
      user: null,   
      username: null,
      email: null,    
      like_movies: [],
    }
  },
  created() {
    this.getUser()
    
  },
  methods: {
    getUser() {
      const token = this.$store.state.token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
        Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        // console.log(res.data)
        this.user = res.data
        this.username = res.data.username
        this.email = res.data.email
        // this.nickname = res.data.nickname
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/users/${this.username}`,
          headers: {
          Authorization: `Token ${token}`
          }
        })
          .then((res) => {
          console.log(res.data)
          this.like_movies = res.data.like_movies
          // this.nickname = res.data.nickname
          })
          .catch((err) => {
            console.log(err)
          })
        })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>
