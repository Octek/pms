
// mobx
import { observer } from "mobx-react-lite";
// components
import IssueNavbar from "components/issues/navbar";

const ProjectLayout = ({ children }: { children: React.ReactNode }) => (
  <div className="relative w-screen min-h-[500px] h-screen overflow-hidden flex flex-col">
    <div className="flex-shrink-0 h-[60px] border-b border-custom-border-300 relative flex items-center bg-custom-sidebar-background-100 select-none">
      <IssueNavbar />
    </div>
    <div className="w-full h-full relative bg-custom-background-90 overflow-hidden">{children}</div>
  </div>
);

export default observer(ProjectLayout);
