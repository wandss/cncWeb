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
      for(let i=0; i<ark.length; i++){
        console.log(ark[i])
        console.log(this.$urls.plot.upload)
        this.$http.post(this.$urls.plot.upload+ark[i].name, ark[i])
          .then(resp=>{
            console.log(resp)
            console.log(resp.data)
          })
          .catch(error=>{
            console.log(error)
            console.log(error.response)
          })
      }
    },
    startPlotting(){
      console.log('Stat Plotting.......')
      console.log('Open Loader')
    }
    /*
    fileUpload(files){
      const config = {
        onUploadProgress:((progressEvent)=>{
          let percentCompleted = Math.round((progressEvent.loaded *100)/
            progressEvent.total);
            this.uploadProgress = percentCompleted
        }),
      }

      for(let i=0; i< files.length; i++){
        this.$http.post(this.$urls.upload+files[i].name, files[i], config)
        .then(resp=>{
          this.uploadedFilesList.push({id:resp.data.id, name:resp.data.filename, disabled:true})
          this.uploadProgress = '0'
          if(i === files.length-1){
            this.allowFnetUpload = true;
          }
        })
        //eslint-disable-next-line
        .catch(error=>{
          console.log(error.response)
          this.uploadProgress = '0'
        })
      }
    },
    uploadToFileNet(canUpload){
      this.$store.commit('setShowLoader', true)
      this.existentFiles = false;
      const data = {documents:this.uploadedFilesList.map(item=>item.id),
        canUpload:canUpload, num_remessa: this.remessa}
      this.uploadedCount = this.uploadedFilesList.length
      this.$http.post(this.$urls.eng.load, data)
        .then(resp=>{
          let title = "Carga Finalizada"
          let message = ''
          console.log(resp.data)
          this.documentsDetails = resp.data.message.detail
          this.alert.showAlert = true
          this.alert.title = title
          this.alert.cssClass = 'success'
          this.alert.message = message
          this.uploadComponentKey ++;
          this.uploadedFilesList = [];
          this.$store.commit('setShowLoader', false)
          }
        )
        .catch(error=>{
          let alertClass = 'danger'
          let title = "Atenção!"
          let message = error.response.data.message

          if(error.response.status === 400){
            alertClass = 'warning'
          }
          else if(error.response.status === 409){
            this.existentFiles = true
            alertClass = 'warning'
            title = "Arquivos já existentes no GED Corporativo:"
          }
          if(Array.isArray(error.response.data.message)){
            message = error.response.data.message.map((item, index) =>{
              return {id:index, value:item, name:item}
            })
          }
          if(error.response.data.has_invalid_codes){
            //Invalid Codes has been passed
            this.hasInvalidCodes = error.response.data.has_invalid_codes
            this.documentsDetails = error.response.data.detail
          }
          this.alert.showAlert = true
          this.alert.message = message
          this.alert.title = title
          this.alert.cssClass = alertClass
          this.uploadComponentKey ++;
          this.uploadedFilesList = [];
          this.$store.commit('setShowLoader', false)
        })
    }
    */
  }
}
</script>
<style scoped>
.home{
  margin-top:2rem;
}
</style>
