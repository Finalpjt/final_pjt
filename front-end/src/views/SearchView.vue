<template>
    <div>
      <h1>Search list</h1>
      <hr>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchView',
    components: {
    },
    computed:{
      isLogin() {
        return this.$store.getters.isLogin // 로그인 여부
      }
    },
    created() {
      this.SearchMovies()
    },
    methods: {
      getSearchMovies() {
        if (this.isLogin) {
          this.$store.dispatch('getSearchMovies')
        } else {
          alert('로그인이 필요한 페이지입니다...')
          this.$router.push({ name: 'HomeView' })
        }
  
  
        // 로그인이 되어 있으면 getArticles action 실행
        // 로그인 X라면 login 페이지로 이동
  
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  