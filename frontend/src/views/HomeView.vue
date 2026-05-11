<script setup>
import Footer from '@/components/Footer.vue';
import HomeNav from '@/components/HomeNav.vue';
import HowToRegister from '@/components/HowToRegister.vue';
import PlacementStatics from '@/components/PlacementStatics.vue';
import { useRouter } from 'vue-router'
import { ref, nextTick, onMounted, onUnmounted } from "vue";
import { gsap } from "gsap";

const var1 = useRouter()
const var2 = ref(null);
const var3 = ref(null);
const var4 = ref(null);
const var5 = ref(null);
const var6 = ref(null);
let var7;



onMounted(async () => {
  await nextTick();

  if (!var2.value) {
    return;
  }

  var7 = gsap.context(() => {
    const tl = gsap.timeline({ defaults: { ease: 'power2.out' } });

    tl.from(var3.value, {
      opacity: 0,
      y: 50,
      duration: 0.9,
      delay: 0.2,
    })
      .from(var4.value, {
        opacity: 0,
        y: 20,
        duration: 0.6,
      }, '-=0.35')
      .from([var5.value, var6.value], {
        opacity: 0,
        y: 12,
        duration: 0.45,
        stagger: 0.08,
      }, '-=0.25');
  }, var2.value);
});

onUnmounted(() => {
  if (var7) {
    var7.revert(); // cleanup
  }
});

function register_lnk() {
  var1.push('/register')
}
</script>

<template>
  <div class="container">
    <HomeNav />
    <main ref="var2">
      <div id="blur">
        <h1 ref="var3">Welcome to the Placement
          Cell</h1>
        <p ref="var4">Students & Recruiters can join us to avail the best placement assistance through our Placement
          Cell
          platform.</p>
        <br>
        <button ref="var5" @click="register_lnk">Register</button><br><br>
        <a ref="var6" href="#faq">have a doubt, see faq</a><br><br>
      </div>
    </main>


    <div id="about">
      <div class="max_dev">
        <h2 style="color: #3b7ca6;padding-bottom: 20px;">About Us</h2>
        <p>We’ve built a placement portal that actually works as hard as you do. By automating the boring stuff, we’ve
          created a direct line between our students and top-tier recruiters. It’s more than just a job board—it’s a
          dynamic
          ecosystem where industry leaders and fresh talent meet to build what’s next. Our mission is simple: get our
          students into roles they love while helping our partners grow.</p>
      </div>
    </div>


    <div id="backg">
      <PlacementStatics />

      <HowToRegister />
      <div id="faq">
      <h2 style="color: #3b7ca6; width: 90%;">Frequently Asked Questions</h2>


      <div>
        <p id="q1">Is registration free?</p>
        <p id="a1" class="a">Yes, Registration is free.</p><br>
        <p id="q2">Can i change my email after registration?</p>
        <p id="a2" class="a">No, You will not be ableto change you email once registered; you can only update your
          profile with extra fields for student like resume, address, phone_no etc.</p>
      </div>
    </div>
    </div>

    

    <!-- -------------------------------------------------register -->
    <div class="register">
      <h1>Ready to shape your future?</h1>

      <p>
        Join thousands of students and hundreds of recruiters who have already transformed
        their career trajectory through our portal.
      </p>

      <div class="buttons">
        <button class="primary" @click="$router.push('/register')">
          Register
        </button>
        <button class="secondary">Contact Support</button>
      </div>
    </div>


    <Footer />
  </div>

</template>

<style scoped>
main {

  /* background-color: #f5f5f5; */
  color: #3b7ca6;
  /* padding: 30px; */
  background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQAI2TCpsdreAC1nfRQrG2nvAMN_3NcsfNww&s');
  background-size: cover;
  background-attachment: fixed;
  /* keeping it stationary */
  background-position: center;
  padding-bottom: 200px;
  padding-top: 200px;


}

#blur{
  background-color: rgba(26, 51, 65, 0.2);
  backdrop-filter: blur(20px);
  padding: 30px;
}

main p {
  color: white;
}

/* h5{
  font-size:xx-large;
} */


#faq p {
  /* padding: 15px; */
  color: gray;
  width: 90%;
}


#faq {
  color: forestgreen;
  /* padding: 30px; */
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding-bottom: 30px;

}

/* .a{
  display: none;
} */

#backg{
  background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZpgdEebc1XupRjHJcloEEw6RqEtxNLc96_Q&s');
  background-repeat: no-repeat;
  background-size: cover;
}

a {
  color: #3b7ca6;
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
  /* display: flex; */
  padding: 30px;
  background-color: #f5f5f5;
  padding-top: 100px;
  padding-bottom: 100px;
}

/* 
h2,
#about h2 {
  align-items: center;
  justify-content: center;
  color: #3b7ca6;


} */

#faq h2 {
  color: #f5f5f5;
}

/* 
#about p {
  align-items: center;
  background-color: #f5f5f5;
  padding: 30px;
  max-width: 660px;
} */

.register {
  background: #3b7ca6;
  color: white;
  text-align: center;
  padding: 80px 20px;
}

.register h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.register p {
  max-width: 650px;
  margin: 0 auto 30px;
  line-height: 1.6;
  font-size: 1rem;
  opacity: 0.9;
  color: white;
}

main h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.max_dev {
  max-width: 1280px;
  margin: 0 auto;
  /* width: 100%; */
}


@media(max-width:660px) {
  main {
    
    padding-bottom: 100px;
    padding-top: 100px;
  }
  #blur{
    padding: 30px;
  }

  main h1 {
    font-size: 2.2rem;
    margin-bottom: 20px;
    color: #3b7ca6;
  }
  #faq{
    padding: 20px;
  }
}
</style>
