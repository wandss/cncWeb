<template>
  <div>
    <nav class="navbar navbar-dark bg-secondary navbar-expand-lg ">
      <button class="navbar-toggler" type="button" @click="showSmMenu=!showSmMenu"
        data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false"
        aria-label="Toggle navigation" >
        <span class="navbar-toggler-icon"></span>
      </button>
      <modal-confirm :show="showModalConfirm" @getConfirmation="logout"
       @close="showModalConfirm=!showModalConfirm" message="Are you sure?"
       title="Signing Out."
      />
      <a class="navbar-brand" href="/login">{{appData?appData.app_name:appData}}</a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/home">
              Home <span class="sr-only">(current)</span>
            </a>
          </li>
          <!--
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle"
             href="#" id="navbarDropdown" role="button"
             data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Dropdown
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
          -->
        </ul>
        <!--
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search"
           placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0"
           type="submit">
            Search
          </button>
        </form>
        -->
        <ul class="navbar-nav">
          <li class="nav-item active text-white" id="username">
            <span class="fa fa-user"></span>
            {{$store.state.username}}
          </li>
        </ul>
        <ul class="navbar-nav" id="logoutBtn">
          <li class="nav-item">
            <button class="btn btn-outline-danger"
             @click="showModalConfirm=true">
              <span class="fa fa-sign-out-alt"></span>
            </button>
          </li>
        </ul>
      </div>
    </nav>
    <sm-menu :show="showSmMenu" :items="smItems" @click="handleSmClick">
    </sm-menu>
  </div>
</template>
<script>
import ModalConfirm from "@/components/ModalConfirm"
import SmMenu from '@/components/SMMenu'
export default{
  name:'Navbar',
  components:{ModalConfirm, SmMenu},
  data(){
    return{
      showModalConfirm:false,
      showSmMenu:false,
      smItems:[],
      appData:null,
    }
  },
  mounted(){
    const logout = 'Logout ('+this.$store.state.username+')'

    this.smItems.push(
      {name: logout, icon: 'fa fa-sign-out-alt',
        event:()=>this.showModalConfirm=!this.showModalConfirm},
    )
    // this.getAppData()
  },
  methods:{
    logout(option){
      if(option){
        this.$store.commit('setShowLoader', true)
        window.localStorage.clear('token')
        window.location.href = '/'
      }
      else{
        this.showModalConfirm = false
      }
    },
    handleSmClick(event){
      this.showSmMenu = !this.showSmMenu
      event()
    },
    getAppData(){
      this.$http.get(this.$urls.frontend.appData)
        .then((resp)=>this.appData=resp.data[0])
        .catch(error=>console.log(error))
    }
  }
}
</script>
<style scoped>
#logoutBtn{
  margin-left:1rem;
}
#username{
  text-transform:capitalize;
}
</style>
