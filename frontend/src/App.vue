<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
// import RegisterView from './views/Auth/RegisterView.vue';
</script>

<template>
  <header>
    <div id="top_bar">
      <div>contact us | +91 6200209997&emsp;</div>
      <div>&emsp;application deadline | 10th April</div>
      
    </div>
  </header>
  <!-- <h5>You Are In Home Page</h5> -->

  <RouterView />
</template>

<style scoped>
body{
  margin: 0px;
  padding: 0px;
}

#top_bar{
  display: flex;
  /* justify-content: space-between; */
  align-items: center;
  justify-content: center;
  background-color: #2980B9;
  color: white;
  padding: 3px;
  /* padding: 2px 30%; */
}


</style>
