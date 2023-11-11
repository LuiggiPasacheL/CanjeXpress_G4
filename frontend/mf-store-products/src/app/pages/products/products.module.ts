import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProductsComponent } from './products.component';
import { ProductCardComponent } from './product-card/product-card.component';


@NgModule({
  declarations: [
    ProductsComponent,
    ProductCardComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports:[
    ProductsComponent
  ]
})
export class ProductsModule { }
