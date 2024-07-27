import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'example';
  topic:string = '';
  items:any[] = [
    {
      value:'Physics'
    },
    {
      value:'Math'
    },
    {
      value:'Chemistry'
    }
  ]

  constructor(){}

  onInit(){

  }

  addInList(){
    this.items.push(
      {
        value:this.topic
      }
    );
  }

  deleteInList(index:number){
    this.items.splice(index,1);
  }
}
