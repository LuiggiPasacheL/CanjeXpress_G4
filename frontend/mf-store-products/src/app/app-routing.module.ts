import { ProductsComponent } from './pages/products/products.component';

import { EmptyRouteComponent } from './empty-route/empty-route.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DetailsComponent } from './pages/products/details/details.component';
import { APP_BASE_HREF } from '@angular/common';

const routes: Routes = [
  {
    path: 'products',
    children:[
      {
        path:'',
        component: ProductsComponent
      },
      {
        path:':productId',
        component: DetailsComponent
      }

    ]},
  { path:'**', component: EmptyRouteComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [{provide: APP_BASE_HREF, useValue: '/'}],
})
export class AppRoutingModule { }
