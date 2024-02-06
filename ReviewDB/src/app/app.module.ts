// app.module.ts
import { NgModule } from '@angular/core';
import { AboutUsModule } from './main-pages/about-us/about-us.module';
import { HeaderModule } from './main-fragments/header/header.module';
import { FooterModule } from './main-fragments/footer/footer.module';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AboutUsModule,
    HeaderModule,
    FooterModule
  ],
  bootstrap: [AppComponent],
})
export class AppModule { }
