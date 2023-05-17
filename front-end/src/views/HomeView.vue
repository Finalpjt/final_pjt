<template>
  <div id="home">
    
    <ul class="">
      <!-- 비 로그인 시  -->
      <div class="navbar-nav ml-auto" v-if="!currentUser">
        <li class="nav-item">
          <router-link to="/signup">
            <font-awesome-icon icon="user-plus" /> Sign Up
          </router-link>
        </li>
        <li class="nav-item">
          <form @submit.prevent="logIn">
            <label for="username">username : </label>
            <input type="text" id="username" v-model="username"><br>

            <label for="password"> password : </label>
            <input type="password" id="password" v-model="password"><br>

            <input type="submit" value="logIn">
          </form>
        </li>
      </div>
      <!-- 로그인 시 -->
      <div class="navbar-nav ml-auto" v-if="currentUser">
        <li class="nav-item">
          <router-link to="/profile">
            <font-awesome-icon icon="user" />
            {{currentUser.username}}
          </router-link>
        </li>
        <li class="nav-item">
          <a href class="nav-link" @click="logout">
            <font-awesome-icon icon="sign-out-alt" /> LogOut
          </a>
        </li>
      </div>
    </ul>
    <MovieList/>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    MovieList,
  },
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    currentUser () {
      return this.$store.state.auth.user
    }
  },
  methods: {
    logOut () {
      this.$store.dispatch('auth/logout')
      this.$router.push('/')
    },
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    }
  }
}
</script>
