<template>
  <div class="container home">
    <div class="form-group">
      <h3>Hello!!!</h3>
      <p>This app controls a Mini CNC Ploting  machine, made with two DVD Drives.</p>
      <p>To start ploting just click the button bellow</p>
       <modal :show="showModal" @click="showModal=false"  modalSize="modal-full"
       title="Start your engines...">
         <div slot="body">
          <progress-bar :progress="uploadProgress" :show="showProgress"/>
          <upload label="Upload GCode File" name="upload"
           @change="handleUpload"
           />
          <i>{{gcode_file}}</i>
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
import ProgressBar from '@/components/Progressbar.vue'

export default {
  name: 'home',
  components: {BaseBtn, Modal, Upload, ProgressBar},
  data(){
    return {
      gcode_file: '',
      showModal: false,
      disabledStartButton: true,
      showProgress: false,
      uploadProgress: 0,
      uploadedFileId: null,
    }
  },
  methods: {
    handleUpload(ark){
      this.uploadProgress = 0
      this.showProgress = true
      const config = {
        onUploadProgress:((progressEvent)=>{
          let percentCompleted = Math.round((progressEvent.loaded *100)/
            progressEvent.total);
            this.uploadProgress = percentCompleted
        }),
      }
      this.disabledStartButton = false
      for(let i=0; i<ark.length; i++){
        this.gcode_file = ark[i].name
        this.$http.post(this.$urls.plot.upload+ark[i].name, ark[i], config)
          .then(resp=>{
            console.log(resp)
            console.log(resp.data)
            this.uploadedFileId = resp.data.id
            this.showProgress = false
          })
          .catch(error=>{
            console.log(error)
            console.log(error.response)
            this.showProgress = false
          })
      }
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
