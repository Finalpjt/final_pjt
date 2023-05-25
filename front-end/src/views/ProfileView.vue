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
    v-for="(like_movie, idx) in like_movies" :key="idx"
    >
    <!-- <p>2번째</p> -->
    <!-- {{ like_movie }} -->
    <div class="card" @click="reload()">
        <router-link :to="{
          name: 'DetailView',
          params: {id: like_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${like_movie?.poster_path}`" alt="" srcset="">
          <!-- <p>아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ</p> -->
          </div>
        </router-link>
    
    </div>
    </div>
    <ul v-if="like_movies!==null">
    <MovieRecommendProfile v-bind:like_movies="like_movies"/>
    </ul>
    </div>
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
            // console.log(res.data)
            // console.log('checkcheckcheckcheckcheckcheck')
        //   console.log(res.data.like_movies)
            // console.log('checkcheckcheckcheckcheckcheck')
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
