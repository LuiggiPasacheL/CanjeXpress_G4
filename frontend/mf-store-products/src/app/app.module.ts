import { EmptyRouteComponent } from './empty-route/empty-route.component';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsModule } from './pages/products/products.module';
import { DetailsModule } from './pages/products/details/details.module';

@NgModule({
  declarations: [
    AppComponent,
    EmptyRouteComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ProductsModule,
    DetailsModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
