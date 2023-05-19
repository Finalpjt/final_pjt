<template>
  <div id="home">
    <h1>Home Page</h1>
    <h2>Login</h2>
    <p v-if="this.isLogin">로그인 중 입니다.</p>
    <form @submit.prevent="login" v-if="!this.isLogin">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="login">
    </form>

<!--   <ul class=""> -->
      <!-- 비 로그인 시  -->
      <!-- <div class="navbar-nav ml-auto" v-if="!currentUser">
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
      로그인 시
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
    </ul> -->

  </div>
</template>

<script>

// @ is an alias to /src

export default {
  name: 'HomeView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
  },
  methods: {
    logout () {
      this.$store.dispatch('/logout')
      this.$router.push('/')
    },
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
      this.$router.push('/signup')
    }
  }
}
</script>
