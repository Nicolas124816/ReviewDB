import { NgModule } from '@angular/core';
import { ContactUsComponent } from './contact-us.component';
import { HeaderModule } from '../../main-fragments/header/header.module';
import { FooterModule } from '../../main-fragments/footer/footer.module';

@NgModule({
  declarations: [
    ContactUsComponent,
  ],
  imports: [
    HeaderModule,
    FooterModule,
  ],
  exports: [
    ContactUsComponent,
  ],
})
export class ContactUsModule { }
