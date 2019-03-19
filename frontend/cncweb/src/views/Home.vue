<template>
  <div class="container home">
    <form action="">
      <div class="form-group">
        <upload label="Upload GCode File" name="upload"
         @change="handleUpload"
        />
        <base-btn type="submit">
          Start Plotting
        </base-btn>
      </div>
    </form>
  </div>
</template>
<script>
import BaseBtn from '@/components/baseButton.vue'
import Upload from '@/components/Upload.vue'
export default {
  name: 'home',
  components: {BaseBtn, Upload},
  data(){
    return {
      uploadedFile: '',
    }
  },
  methods: {
    handleUpload(ark){
      console.log(ark)
    }
  }
}
</script>
<style scoped>
.home{
  margin-top:2rem;
}
</style>
