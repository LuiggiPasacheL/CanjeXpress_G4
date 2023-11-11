import { Observable } from 'rxjs';
import { ProductsService } from './../services/products.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../interfaces/product.interface';
import {Location} from '@angular/common';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})
export class DetailsComponent implements OnInit {
  product$!:Observable<Product>;
  productId!:number;

  constructor(
    private readonly route: ActivatedRoute,
    private readonly productsSvc:ProductsService,
    private readonly location:Location,
  ) { }

  ngOnInit() {
    this.productId = this.route.snapshot.params?.['productId'];
    this.product$ = this.productsSvc.getProductById(this.productId);
  }

  goBack():void {
    this.location.back();
  }

}
