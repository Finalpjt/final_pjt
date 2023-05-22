<template>
    <div>
      <h1>Search list</h1>
      카드로 만들어서 들어가도록?
      <hr>
        <div v-for="search_movie in this.search_movies" :key="search_movie.id" :search_movie="search_movie">
            <p><img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${search_movie.poster_path}`" alt="" srcset=""></p>
            <p>{{ search_movie.title }}</p>
            <p></p>
            <p>{{ search_movie.vote_average }}</p>
            <router-link :to="{
            name: 'DetailView',
            params: {id: search_movie.id }}">
            DETAIL
            </router-link>
        </div>
        adult, backdrop_path, genre_ids, id, original_language,... 

    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchView',
    data(){
        return {
            search_movies: this.$store.state.search_movies
        }
    },
    components: {
    },
    computed:{
      isLogin() {
        return this.$store.getters.isLogin // 로그인 여부
      }
    },
    created() {
      this.getSearchMovies()
    },
    methods: {
      getSearchMovies() {
        if (this.isLogin) {
            console.log(this.$store.state.search_movies)
        //   this.$store.dispatch('getSearchMovies')
        } else {
          alert('로그인이 필요한 페이지입니다...')
        }
  
  
        // 로그인이 되어 있으면 getArticles action 실행
        // 로그인 X라면 login 페이지로 이동
  
      },

    }
  }
  </script>
  
  <style>
  
  </style>
  