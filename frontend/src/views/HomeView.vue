<script setup>
import HomeNav from '@/components/HomeNav.vue';
import { useRouter } from 'vue-router'

const router = useRouter()

function register_lnk() {
  router.push('/register')
}
</script>

<template>
  <HomeNav/>
  <main>
    <h5>Welcome to the Placement Cell</h5>
    <p>Students & Recruiters can join us to avail the best placement assistance through our Placement Cell platform.</p><br>
    <button @click="register_lnk">Register</button>
  </main>
</template>

<style scoped>
main{
  margin-top: 50px;
  /* background-color: #f5f5f5; */
  color: #2980B9;
  padding:20px;
}
h5{
  font-size:xx-large;
}
p{
  color: black;
}
</style>
