<script setup>
import Footer from '@/components/Footer.vue';
import HomeNav from '@/components/HomeNav.vue';
import HowToRegister from '@/components/HowToRegister.vue';
import PlacementStatics from '@/components/PlacementStatics.vue';
import { useRouter } from 'vue-router'

const router = useRouter()

function register_lnk() {
  router.push('/register')
}
</script>

<template>
  <HomeNav />
  <main>
    <h1>Welcome to the <span style="background-color: #2980b9;color: #f5f5f5;opacity: 0.7;">Placement Cell</span></h1>
    <p>Students & Recruiters can join us to avail the best placement assistance through our Placement Cell platform.</p>
    <br>
    <button @click="register_lnk">Register</button><br><br>
    <a href="#faq">have a doubt, see faq</a><br><br>
  </main>

  <div id="pattern">
    <div id="about">
      <h2>About Us</h2>
      <p>We’ve built a placement portal that actually works as hard as you do. By automating the boring stuff, we’ve created a direct line between our students and top-tier recruiters. It’s more than just a job board—it’s a dynamic ecosystem where industry leaders and fresh talent meet to build what’s next. Our mission is simple: get our students into roles they love while helping our partners grow.</p>
    </div>

  </div>
  <PlacementStatics />

  <HowToRegister />

  <div id="faq">
    <h2>Frequently Asked Questions</h2>
    

    <div>
      <p>Is registration free?<br>Yes, Registration is free.</p>
      <p>Can i change my email after registration? <br>No, You will not be ableto change you email once registered; you can only update your profile with extra fields for student like resume, address, phone_no etc.</p>
    </div>
  </div>
  <Footer/>
  
</template>

<style scoped>
main {
  margin-top: 50px;
  /* background-color: #f5f5f5; */
  color: #2980B9;
  padding: 20px;
}

/* h5{
  font-size:xx-large;
} */
 p{
  color: gray;
 }

#faq p {
  padding: 15px;
  color: #f5f5f5;
}


#faq {
  background: linear-gradient(150deg,forestgreen,white);
  padding: 30px;

}


a {
  color: #2980B9;
  padding-top: 5px;
  /* text-decoration: underline; */
}

a:hover {
  color: cadetblue;
  text-decoration: overline;
  /* text-decoration: underline; */

}

#about {
  /* justify-content: center; */
  /* max-width: 900px; */
  /* margin: 0 auto; */
  align-items: center;
  display: flex;
  padding: 30px;
  background-color: #f5f5f5;
}
h2,
#about h2 {
  /* align-items: center; */
  /* justify-content: center; */
  color: #2980B9;

}

#faq h2{
  color: #f5f5f5;
}

#about p {
  /* align-items: center; */
  /* background-color: #f5f5f5; */
  padding: 30px;
}



#pattern{
  background-image: url('../assets/pattern_line.png');
  background-repeat: repeat;
  background-size: auto;
  background-position: top left;
}
</style>
