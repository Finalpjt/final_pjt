<template>
  <div>
    <h1>Main Page</h1>
    <MovieList />
    <hr>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MainView',
  components: {
    MovieList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getTodayMovies()
  },
  methods: {
    getTodayMovies() {
      if (this.isLogin) {
        this.$store.dispatch('getTodayMovies')
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
