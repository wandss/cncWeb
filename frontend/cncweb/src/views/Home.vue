<template>
  <div class="container home">
    <div class="form-group">
      <h3>Hello!!!</h3>
      <p>This app controls a Mini CNC Ploting  machine, made with two DVD Drives.</p>
      <p>To start ploting just click the button bellow</p>
       <modal :show="showModal" @click="showModal=false"  modalSize="modal-lg"
       title="Start your engines...">
         <div slot="body">
          <upload label="Upload GCode File" name="upload"
           @change="handleUpload"
           />
         </div>
         <div slot="footer" >
          <base-btn cssClass="btn btn-warning" :disabled="disabledStartButton"
            @click="startPlotting">
            Start Plotting
          </base-btn>
         </div>
       </modal>
      <base-btn @click="showModal=!showModal">
        Start Plotting
      </base-btn>
    </div>
  </div>
</template>
<script>
import BaseBtn from '@/components/baseButton.vue'
import Modal from '@/components/Modal.vue'
import Upload from '@/components/Upload.vue'
export default {
  name: 'home',
  components: {BaseBtn, Modal, Upload},
  data(){
    return {
      uploadedFile: '',
      showModal: false,
      disabledStartButton: true,
    }
  },
  methods: {
    handleUpload(ark){
      console.log(ark)
      this.disabledStartButton = false
    },
    startPlotting(){
      console.log('Stat Plotting.......')
      console.log('Open Loader')
    }
  }
}
</script>
<style scoped>
.home{
  margin-top:2rem;
}
</style>
