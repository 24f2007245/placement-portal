<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
// import RegisterView from './views/Auth/RegisterView.vue';
</script>

<template>
  <header>
    <div id="top_bar">
      <div class="top_ele" id="rm">Contact Us | +91 6200999999 , +91 9900620099&emsp;</div>
      <div class="top_ele">Application Deadline | 10th April </div>
      
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
  justify-content:center;
  background-color: #f5f5f5;
  color: #2980b9;
  padding: 3px;
  gap: 150px;

}
.top_ele{
  padding-left: 20px;
}
@media(max-width:790px){
  #top_bar{
   gap: 20px;
  }
}
@media(max-width:500px){
  /* overflow: hidden; */
  #rm{
    display: none;
  }
  #top_bar{
    display: block;
  }

}


</style>
