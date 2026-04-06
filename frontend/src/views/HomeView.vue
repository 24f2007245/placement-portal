<script setup>
import Footer from '@/components/Footer.vue';
import HomeNav from '@/components/HomeNav.vue';
import HowToRegister from '@/components/HowToRegister.vue';
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
      <p>Our Placement Portal offers a seamless and fully automated operational process for both students and
        recruiters. This dynamic platform efficiently connects our students with leading job opportunities, while
        providing recruiters with an automated and streamlined experience. Beyond traditional placement assistance, the
        portal actively collaborates with industries committed to making a significant impact. Our core focus remains on
        securing the best job offerings for our students while contributing to the growth and development of the broader
        learning community. [source- IITM BS placement Portal]</p>
    </div>

  </div>

  <HowToRegister />

  <div id="faq">
    <h2>Frequently Asked Questions</h2>
    <p>For Students</p>

    <div>
      <p>Is registration free?<br>Yes, it's completely free.</p>
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
}

#faq {
  background-color: #f5f5f5;
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
