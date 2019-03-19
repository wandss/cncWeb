class ChartUtils{
  constructor(data, lineTension=0, fill=false){
    this.data = data;
    this.datasets = {labels:[], data:[]};
    this.lineTension = lineTension;
    this.fill = fill;
    this.r = 2;
    this.g = 35;
    this.b = 185;
  }
  setDataset(chartType){
    /*Extracts data from the data Array and creates
     * datasets objects as expected by Chart.js */

    //let data = []
    //let newRow = {}
    if(chartType === 'scatter'){
      /*Replace column names by, x and y*/

      this.datasets.data.push(
        {data:[
          {x:8.7, y:98.3},
          {x:9.2, y:70.1},
          {x:9, y:60.2},
          {x:8.9, y:61.2},
          {x:9, y:41.7},
          {x:8.9, y:51.9},
          {x:9.1, y:41.7},
        ]}
      )
    }
    else{
      Object.keys(this.data[0]).forEach(col=>{
        if(!isNaN(this.data[0][col])){
          this.datasets.data.push({
              label:col,
              data:this.data.map(item=>item[col]),
              borderWidth:1,
              fill:this.fill,
              lineTension:this.lineTension,//0.1 to 1
              pointHitRadius:150,
          })
        }
        else{
          this.datasets.labels = this.data.map(item=>item[col])
        }
      })
    }
    if(this.cartType === 'bubble'){
      this.__calculateBubbleRadius()
    }
    this.__setDatasetColors(chartType)
  }
  __setDatasetColors(chartType){
      let alpha = chartType==='pie'?'0.5':'0.4';
      let backgroundColor = [];
      const datasetsCount = chartType==='pie'?
          this.datasets.labels.length:
          this.datasets.data.map(item=>item.label).length;

      for(let i=0; i< datasetsCount; i++){
          if(this.g <1){
              this.g = -5
          }
          if(this.r > 255){
              this.r = -10
          }
          if(this.b > 255){
              this.b = 150
          }

        /*
          this.g -= 35;
          this.r += 17;
          this.b += 1;
          */

          this.r = Math.floor(Math.random()*(255 - 0 +1)) + 1;
          this.g = Math.floor(Math.random()*(255 - 0 +1)) + 1;
          this.b = Math.floor(Math.random()*(255 - 0 +1)) + 1;
          backgroundColor.push(
              'rgba('+[this.r,this.g,this.b].join(',')+','+alpha+')');

          /*const [r,g,b] = [Math.floorthis.(Math.random()*256, +1),
          Math.floor(Math.random()*256, +1),
          Math.floor(Math.random()*256, +1),
          ];
          Math.floor(Math.random() * (max - min + 1)) + min;
          */
      }

      if(chartType ==='pie'){
          this.datasets.data[0].backgroundColor = backgroundColor
      }
      else{
          this.datasets.data.forEach((item, index)=>{
              item.backgroundColor = backgroundColor[index];
              item.borderColor = backgroundColor[index];
              if(this.fill){
                  item.borderColor = 'rgba(255, 255, 255, 0.6)';
              }
          })
      }
  }
  __calculateBubbleRadius(){
      console.log('YAY')
      console.log(this.datasets.data[0])
  }

  /*SCATTER DATA SAMPLE
  label:'Block one',
  data:[
      {x:20, y:2, r:5},
      {x:21, y:3, r:6},
      {x:22, y:4, r:7}
  ],*/

  //data:{
  //    datasets:[{
  //        data:[
  //            {x:20, y:2, r:5},
  //            {x:21, y:3, r:6},
  //            {x:21.1, y:3.5, r:6},
  //            {x:21.2, y:3.6, r:6},
  //            {x:22, y:4, r:7}
  //        ],
  //    }],
  //}
}

export default ChartUtils;
