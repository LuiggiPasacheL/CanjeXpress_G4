import { Injectable } from '@angular/core';
import { empty, Observable, of } from 'rxjs';
import { Product } from '../interfaces/product.interface';

// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getFirestore, collection, getDocs } from 'firebase/firestore';

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBs_9dsYiDN16wGw8Tm3EwqperjpUxY--M",
  authDomain: "g5-arquitectura.firebaseapp.com",
  projectId: "g5-arquitectura",
  storageBucket: "g5-arquitectura.appspot.com",
  messagingSenderId: "734139387824",
  appId: "1:734139387824:web:7dba57e18a3447f24ad075",
  measurementId: "G-707LK21PSY"
};
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

@Injectable({ providedIn: 'root' })
export class ProductsService {
  private readonly products: Product[] = [/* Your existing products array */];

  public getProducts(): Observable<Product[]> {
    // Check if you want to use Firestore or the existing products array
    const useFirestore = true; // Set this to true if you want to use Firestore

    if (useFirestore) {
      return this.getFirestoreProducts();
    } else {
      return of(this.products);
    }
  }

  public getProductById(id: number): Observable<Product> {
    const productFound = this.products.find((product) => product.id === +id);
    return productFound ? of(productFound) : empty();
  }

  private getFirestoreProducts(): Observable<Product[]> {
    const db = getFirestore(app);
    const productosRef = collection(db, 'productos');

    return new Observable((observer) => {
      getDocs(productosRef)
        .then((querySnapshot) => {
          const firestoreProducts: Product[] = [];

          querySnapshot.forEach((doc) => {
            const data = doc.data() as Product;
            firestoreProducts.push(data);
          });

          observer.next(firestoreProducts);
          observer.complete();
        })
        .catch((error) => {
          console.error('Error fetching Firestore products:', error);
          observer.error(error);
        });
    });
  }
}
