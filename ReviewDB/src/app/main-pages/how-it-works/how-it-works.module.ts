import { NgModule } from '@angular/core';
import { HowItWorksComponent } from './how-it-works.component';
import { HeaderModule } from '../../main-fragments/header/header.module';
import { FooterModule } from '../../main-fragments/footer/footer.module';

@NgModule({
  declarations: [
    HowItWorksComponent,
  ],
  imports: [
    HeaderModule,
    FooterModule,
  ],
  exports: [
    HowItWorksComponent,
  ],
})
export class HowItWorksModule { }
