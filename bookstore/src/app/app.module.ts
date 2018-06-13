import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { GridBookComponent } from './components/grid-book/grid-book.component';
import { BookListComponent } from './components/book-list/book-list.component';
import { BookDetailComponent } from './components/book-detail/book-detail.component';
import { AppRoutingModule } from './router/app-routing.module';
import { ApiService } from './service/api.service';
import { BookService } from './service/book/book.service';
import { HttpClientModule } from '@angular/common/http'; 


@NgModule({
  declarations: [
    AppComponent,
    GridBookComponent,
    BookListComponent,
    BookDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    ApiService, 
    BookService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
