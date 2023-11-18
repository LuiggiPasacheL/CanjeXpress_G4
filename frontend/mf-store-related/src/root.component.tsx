import { RelatedProducts } from "./components/product/related-products";

export default function Root() {
  const pathname = window.location.pathname; 
  const pathnameToArray = pathname.split('/');
  const [first, path, productId] = pathnameToArray;

  return (<RelatedProducts productId={productId} />);
}
