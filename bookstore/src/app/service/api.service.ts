import {Injectable} from "@angular/core";
import { HttpParams, HttpHeaders, HttpClient } from "@angular/common/http";

@Injectable()
export class ApiService {

  private api: any;

  constructor(private http: HttpClient) {
    this.api = 'http://127.0.0.1:8888';
  }

  public call(httpVerb, apiRoute, data = null, params: HttpParams = null, content_type= null) {

    httpVerb = httpVerb || '';
      if (!apiRoute.includes(this.api)){
        apiRoute = (this.api + apiRoute) || '';
      }
      data = data || {};
      const headers = new HttpHeaders();

      if (content_type == true) {
        headers.set("Content-Type", "application/json")
      }

      let successCb = function (resolve) {
        return resolve;
      };

      let errorCb = function (reject) {
        return reject;
      };

      return new Promise((resolve, reject) => {
        if (httpVerb === 'get') {
          this.http.get(apiRoute, {headers: headers, params: params})
            .subscribe(
              data => successCb(resolve(data)),
              err => errorCb(reject(err))
            );
        }

        if (httpVerb === 'post') {
          this.http.post(apiRoute, data, {headers})
            .subscribe(
              data => successCb(resolve(data)),
              err => errorCb(err)
            );
        }

        if (httpVerb === 'put') {
          this.http.put(apiRoute, data, {headers})
            .subscribe(
              data => successCb(resolve(data)),
              err => errorCb(err)
            );
        }

        if (httpVerb === 'delete') {
          this.http.delete(apiRoute, {headers})
            .subscribe(
              data => successCb(resolve(data)),
              err => errorCb(err)
            );
        }
      });
  }

}

