import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  // private apiUrl = 'http://localhost:8080/domestic_imports/';

  // constructor(private http: HttpClient) {}

  // postDomesticImports(data: { origin: string; timeframe: number[] }): Observable<any> {
  //   return this.http.post(this.apiUrl, data);
  // }

  private baseURL = 'http://127.0.0.1:8080';

  constructor(private http: HttpClient) {}

  postDomesticImports(data: { origin: string; timeframe: number[] }): Observable<Blob> {
    // Set the response type to Blob for file downloads
    const apiUrl = this.baseURL + '/domestic_exports/';
    return this.http.post(apiUrl, data, { responseType: 'blob' });
  }

  loadCommodityDetails(): Observable<any> {
    const apiUrl = this.baseURL + '/get_commodity/';
    return this.http.get<any>(apiUrl);  // Adjust the return type if known
  }

  loadTranspotationDetails(): Observable<any> {
    const apiUrl = this.baseURL + '/get_transpotation/';
    return this.http.get<any>(apiUrl);  // Adjust the return type if known
  }

  loadDomesticOriginDetails(): Observable<any> {
    const apiUrl = this.baseURL + '/get_domestic_origin/';
    return this.http.get<any>(apiUrl);  // Adjust the return type if known
  }

  loadDomesticDestinationDetails(): Observable<any> {
    const apiUrl = this.baseURL + '/get_domestic_destination/';
    return this.http.get<any>(apiUrl);  // Adjust the return type if known
  }
  
}
